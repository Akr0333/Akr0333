import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Supabase Auth App',
  description: 'Next.js authentication with Supabase',
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>
}
