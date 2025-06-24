'use client'
import { useEffect, useState } from 'react'
import { useUser } from '@clerk/nextjs'
import { Progress } from '@/components/ui/progress'

export default function Home() {
  const { user } = useUser()
  const userId = user?.id
  const [tasks, setTasks] = useState<{ id: number; title: string; completed: boolean }[]>([])
  const [topic, setTopic] = useState('')
  const [suggestions, setSuggestions] = useState<string[]>([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (userId) fetchTasks(userId)
  }, [userId])

  const fetchTasks = async (uid: string) => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/tasks/${uid}`)
    const data = await res.json()
    // Ensure every task has id, title, completed
    setTasks(data.map((t: any) => ({ id: t.id, title: t.title, completed: t.completed })))
  }

  // Progress calculation
  const total = tasks.length
  const completedCount = tasks.filter(t => t.completed).length
  const percent = total ? Math.round((completedCount / total) * 100) : 0

  const handleGenerate = async () => {
    if (!topic) return alert('Please enter a topic')
    setLoading(true)
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic })
      })
      const body = await res.json()
      setSuggestions(body.tasks)
    } catch (e) {
      console.error(e)
      alert('Generate failed')
    } finally {
      setLoading(false)
    }
  }

  const handleSave = async (title: string) => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/tasks`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, userId })
    })
    if (res.ok) {
      fetchTasks(userId!)
      setSuggestions(prev => prev.filter(s => s !== title))
    }
  }

  const updateTask = async (id: number, data: Partial<{ title: string; completed: boolean }>) => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/tasks/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    if (res.ok) fetchTasks(userId!)
  }

  const handleDelete = async (id: number) => {
    if (confirm('Delete this task?')) {
      await fetch(`${process.env.NEXT_PUBLIC_API_URL}/tasks/${id}`, { method: 'DELETE' })
      fetchTasks(userId!)
    }
  }

  const toggleComplete = (id: number, completed: boolean) => {
    updateTask(id, { completed })
  }

  const handleEdit = (id: number, currentTitle: string) => {
    const newTitle = prompt('Edit title', currentTitle)
    if (newTitle && newTitle !== currentTitle) {
      updateTask(id, { title: newTitle })
    }
  }

  if (!user) return <main className="p-8">Please sign in to view your tasks.</main>

  return (
    <main className="p-6 space-y-8">
      {/* Task List */}
      <section>
        <h1 className="text-2xl mb-2">Your Tasks</h1>
        {total === 0 ? (
          <p>No tasks yet.</p>
        ) : (
          <ul className="space-y-2">
            {tasks.map(t => (
              <li key={t.id} className="px-3 py-2 rounded border flex items-center justify-between">
                <span className={`flex-1 ${t.completed ? 'line-through text-gray-500' : ''}`}>
                  {t.title}
                </span>
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => toggleComplete(t.id, !t.completed)}
                    className="text-sm"
                  >
                    {t.completed ? 'Undo' : 'Done'}
                  </button>
                  <button
                    onClick={() => handleEdit(t.id, t.title)}
                    className="text-sm"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => handleDelete(t.id)}
                    className="text-sm text-red-600 hover:underline"
                  >
                    Delete
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </section>

      {/* Progress Visualization */}
      <section className="mt-6">
        <h2 className="text-lg font-medium mb-1">Your Progress</h2>
        <Progress value={percent} className="w-full" />
        <p className="text-sm text-muted-foreground mt-1">
          {completedCount} of {total} tasks completed ({percent}%)
        </p>
      </section>

      {/* AI-Generated Suggestions */}
      <section>
        <h2 className="text-xl mb-2">Generate AI Tasks</h2>
        <div className="flex gap-2 mb-2">
          <input
            type="text"
            value={topic}
            onChange={e => setTopic(e.target.value)}
            className="border p-2 flex-1"
            placeholder="Enter topic (e.g. Learn Python)"
          />
          <button
            onClick={handleGenerate}
            disabled={loading}
            className="bg-indigo-600 text-white px-4 py-2 rounded disabled:opacity-50"
          >
            {loading ? 'Generating…' : 'Generate'}
          </button>
        </div>
        {suggestions.length > 0 && (
          <ul className="mt-4 space-y-2">
            {suggestions.map((s, idx) => (
              <li key={idx} className="flex justify-between items-center">
                <span>{s}</span>
                <button
                  onClick={() => handleSave(s)}
                  className="text-sm text-blue-600 hover:underline ml-4"
                >
                  Save
                </button>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  )
}
