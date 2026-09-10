import Link from 'next/link'

export default function Home() {
  return <main><div className="card"><h1>Supabase Auth App</h1><p className="muted">Secure email/password authentication with protected routes.</p><p><Link href="/login">Log in</Link> · <Link href="/signup">Create account</Link></p></div></main>
}
