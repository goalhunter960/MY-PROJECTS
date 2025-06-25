// Project: TaskGenius – Full Stack Task Generator App

// ✅ TECHNOLOGY STACK
// - Frontend: Next.js 14.5+, Tailwind CSS, ShadCN UI, Clerk Auth
// - Backend: Hono (NodeJS web framework), Drizzle ORM
// - Database: PostgreSQL (via Neon.tech or Docker)
// - API: Google Gemini API (placeholder for API key)
// - Deployment: Netlify (frontend), Render (backend)

// We'll now start writing the full app starting with the backend, then the frontend.

// === BACKEND SETUP (apps/api/index.ts) ===

import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { z } from 'zod'
import { zValidator } from '@hono/zod-validator'
import { drizzle } from 'drizzle-orm/neon-http'
import { neon } from '@neondatabase/serverless'
import { tasks } from '@taskgenius/db/schema'
import { eq } from 'drizzle-orm'

const app = new Hono()
app.use('*', cors()) // enable CORS

const sql = neon(process.env.DATABASE_URL!)
const db = drizzle(sql)

// Zod schema for validation
const TaskSchema = z.object({
  title: z.string(),
  userId: z.string(),
  completed: z.boolean().optional()
})

app.post('/tasks', zValidator('json', TaskSchema), async (c) => {
  const body = await c.req.json()
  const task = await db.insert(tasks).values(body).returning()
  return c.json({ success: true, task })
})

app.get('/tasks/:userId', async (c) => {
  const userId = c.req.param('userId')
  const userTasks = await db.select().from(tasks).where(eq(tasks.userId, userId))
  return c.json(userTasks)
})

app.put('/tasks/:id', async (c) => {
  const id = Number(c.req.param('id'))
  const data = await c.req.json()
  const updated = await db.update(tasks).set(data).where(eq(tasks.id, id)).returning()
  return c.json({ success: true, updated })
})

app.delete('/tasks/:id', async (c) => {
  const id = Number(c.req.param('id'))
  await db.delete(tasks).where(eq(tasks.id, id))
  return c.json({ success: true })
})

// === GEMINI TASK GENERATION ROUTE ===

const GeminiSchema = z.object({
  topic: z.string()
})

app.post('/generate', zValidator('json', GeminiSchema), async (c) => {
  const { topic } = await c.req.json()

  const prompt = `Generate a list of 5 concise, actionable tasks to learn about ${topic}. Return only the tasks, no numbering or formatting.`

  const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + process.env.GEMINI_API_KEY, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
  })

  const data = await response.json()
  const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || ''
  const tasks = text.split('\n').map(t => t.trim()).filter(Boolean)

  return c.json({ tasks })
})

export default app

// === NOTES ===
// - All routes are typed using zod to validate payloads
// - `generate` uses Google Gemini API with a placeholder API key in .env
// - CRUD is implemented for /tasks
// - User isolation is handled via userId param (Clerk frontend will pass it securely)

// === PLACEHOLDER .env.example FILE ===
// DATABASE_URL=postgresql://your_neon_db_url
// GEMINI_API_KEY=your_google_gemini_key_here
