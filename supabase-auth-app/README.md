# Supabase Auth App

A Next.js App Router starter using Supabase Auth with cookie-based SSR sessions and protected routes.

## Features

- Email/password sign up and login
- Email confirmation callback
- Protected `/dashboard` route
- Logout
- Server-side auth verification with `getClaims()`
- Supabase SSR cookie session handling

## Setup

1. Run `npm install`.
2. Copy `.env.example` to `.env.local`.
3. Add your Supabase project URL and publishable key.
4. Configure the Supabase Auth email template to use:

```text
{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email
```

5. Run `npm run dev` and open `http://localhost:3000`.

## Routes

- `/` public landing page
- `/login` public login page
- `/signup` public signup page
- `/dashboard` protected page
- `/auth/confirm` email confirmation callback

## Security

Keep credentials in `.env.local` and never commit secrets. The app uses the Supabase publishable key on the client and verifies authenticated requests server-side with `getClaims()`.

## Architecture

`lib/supabase/client.ts` creates the browser client, `lib/supabase/server.ts` creates the server client, and `proxy.ts` refreshes sessions and redirects unauthenticated users away from protected routes.
