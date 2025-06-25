'use client'
import { useEffect, useState } from 'react'
import { useUser } from '@clerk/nextjs'
import { Progress } from '@/components/ui/progress'

type Task = {
  id: number
  title: string
  completed: boolean
}

export default function Home() {
  const { user } = useUser()
  const userId = user?.id
  const [tasks, setTasks] = useState<Task[]>([])
  const [topic, setTopic] = useState('')
  const [suggestions, setSuggestions] = useState<string[]>([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (userId) fetchTasks(userId)
  }, [userId])

  const fetchTasks = async (uid: string) => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/tasks/${uid}`)
    const data: Task[] = await res.json()
    setTasks(data)
  }

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
        body: JSON.stringify({ topic }),
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
      body: JSON.stringify({ title, userId }),
    })
    if (res.ok) {
      fetchTasks(userId!)
      alert('Task saved')
    }
  }

  if (!user) return <main className="p-8">Please sign in to view your tasks.</main>

  return (
    <main className="p-6 space-y-8">
      <section>
        <h1 className="text-2xl mb-2">Your Tasks</h1>
        {tasks.length === 0 ? (
          <p>No tasks yet.</p>
        ) : (
          <ul className="space-y-2">
            {tasks.map((t) => (
              <li
                key={t.id}
                className={`px-3 py-2 rounded border ${t.completed ? 'bg-green-100' : 'bg-white'}`}
              >
                {t.title}
              </li>
            ))}
          </ul>
        )}
        <div className="mt-4">
          <Progress value={percent} />
          <p className="mt-1 text-sm text-gray-600">{percent}% completed</p>
        </div>
      </section>

      <section>
        <h2 className="text-xl mb-2">Generate AI Tasks</h2>
        <input
          type="text"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          className="border p-2 mr-2"
          placeholder="Enter topic (e.g. Learn Python)"
        />
        <button
          onClick={handleGenerate}
          disabled={loading}
          className="bg-indigo-600 text-white px-4 py-2 rounded disabled:opacity-50"
        >
          {loading ? 'Generating…' : 'Generate'}
        </button>

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

