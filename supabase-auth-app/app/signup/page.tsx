'use client'

import { FormEvent, useState } from 'react'
import { createClient } from '@/lib/supabase/client'
import Link from 'next/link'

export default function SignupPage() {
  const supabase = createClient()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')

  async function submit(event: FormEvent) {
    event.preventDefault(); setError(''); setMessage('')
    const { error } = await supabase.auth.signUp({ email, password, options: { emailRedirectTo: `${window.location.origin}/auth/confirm` } })
    if (error) setError(error.message)
    else setMessage('Account created. Check your email if confirmation is enabled.')
  }

  return <main><div className="card"><h1>Create account</h1><form onSubmit={submit}><label>Email</label><input type="email" required value={email} onChange={e => setEmail(e.target.value)} /><label>Password</label><input type="password" required minLength={6} value={password} onChange={e => setPassword(e.target.value)} /><button>Create account</button>{error && <p className="error">{error}</p>}{message && <p>{message}</p>}</form><p className="muted">Already registered? <Link href="/login">Log in</Link></p></div></main>
}
