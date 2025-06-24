// === BACKEND ENTRYPOINT ===

import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { z } from 'zod'
import { zValidator } from '@hono/zod-validator'
import { drizzle } from 'drizzle-orm/neon-http'
import { neon } from '@neondatabase/serverless'
import { tasks } from './schema.js'
import { eq } from 'drizzle-orm'
import * as dotenv from 'dotenv'
import { serve } from '@hono/node-server'

// Load environment variables from .env
dotenv.config()

// Initialize Hono app and enable CORS
const app = new Hono()
app.use('*', cors())

// Connect to Neon Postgres using Drizzle ORM
const sql = neon(process.env.DATABASE_URL!)
const db = drizzle(sql)

// Zod schema to validate task data
const TaskSchema = z.object({
  title: z.string(),
  userId: z.string(),
  completed: z.boolean().optional(),
})

// === CRUD Routes for Tasks ===

// Create Task
app.post('/tasks', zValidator('json', TaskSchema), async (c) => {
  const body = await c.req.json()
  const task = await db.insert(tasks).values(body).returning()
  return c.json({ success: true, task })
})

// Get Tasks for a User
app.get('/tasks/:userId', async (c) => {
  const userId = c.req.param('userId')
  const userTasks = await db.select().from(tasks).where(eq(tasks.userId, userId))
  return c.json(userTasks)
})

// Update a Task
app.put('/tasks/:id', async (c) => {
  const id = Number(c.req.param('id'))
  const data = await c.req.json()
  const updated = await db.update(tasks).set(data).where(eq(tasks.id, id)).returning()
  return c.json({ success: true, updated })
})

// Delete a Task
app.delete('/tasks/:id', async (c) => {
  const id = Number(c.req.param('id'))
  await db.delete(tasks).where(eq(tasks.id, id))
  return c.json({ success: true })
})

// === Gemini AI Task Generation ===

const GeminiSchema = z.object({ topic: z.string() })

app.post('/generate', zValidator('json', GeminiSchema), async (c) => {
  const { topic } = await c.req.json()
  const prompt = `Generate a list of 5 concise, actionable tasks to learn about ${topic}. Return only the tasks, no numbering or formatting.`

  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${process.env.GEMINI_API_KEY}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        contents: [
          {
            parts: [{ text: prompt }],
          },
        ],
      }),
    }
  )

  const data = await response.json()
  console.log("Gemini API response raw:", data)

  const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || ''
  const generatedTasks = text.split('\n').map(t => t.trim()).filter(Boolean)

  return c.json({ tasks: generatedTasks })
})

// === Start Server ===
serve(
  {
    fetch: app.fetch,
    port: 3001,
  },
  () => {
    console.log('🚀 Server is running at http://localhost:3001')
  }
)
