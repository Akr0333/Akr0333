'use client'

import { FormEvent, useState } from 'react'
import { createClient } from '@/lib/supabase/client'
import Link from 'next/link'
import { useRouter } from 'next/navigation'

export default function LoginPage() {
  const router = useRouter()
  const supabase = createClient()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  async function submit(event: FormEvent) {
    event.preventDefault(); setLoading(true); setError('')
    const { error } = await supabase.auth.signInWithPassword({ email, password })
    if (error) setError(error.message)
    else router.push('/dashboard')
    router.refresh(); setLoading(false)
  }

  return <main><div className="card"><h1>Log in</h1><form onSubmit={submit}><label>Email</label><input type="email" required value={email} onChange={e => setEmail(e.target.value)} /><label>Password</label><input type="password" required minLength={6} value={password} onChange={e => setPassword(e.target.value)} /><button disabled={loading}>{loading ? 'Logging in...' : 'Log in'}</button>{error && <p className="error">{error}</p>}</form><p className="muted">No account? <Link href="/signup">Sign up</Link></p></div></main>
}
