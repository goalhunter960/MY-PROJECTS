import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const publicRoutes = createRouteMatcher(['/sign-in(.*)', '/sign-up(.*)'])

export default clerkMiddleware(async (auth, req) => {
  if (!publicRoutes(req)) {
    await auth.protect()  // <-- updated here
  }
})

export const config = {
  matcher: ['/((?!_next|static|favicon.ico).*)', '/api(.*)'],
}

