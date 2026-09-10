import { createClient } from '@/lib/supabase/server'
import { redirect } from 'next/navigation'
import LogoutButton from './logout-button'

export const dynamic = 'force-dynamic'

export default async function DashboardPage() {
  const supabase = await createClient()
  const { data: claims } = await supabase.auth.getClaims()
  if (!claims?.claims?.sub) redirect('/login')

  return <main><div className="card"><h1>Protected Dashboard 🔐</h1><p>You are authenticated.</p><p className="muted">User ID: {String(claims.claims.sub)}</p><LogoutButton /></div></main>
}
