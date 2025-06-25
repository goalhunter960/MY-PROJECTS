import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware((auth, req) => {
  return auth().then((session) => {
    if (!session.userId) {
      return new Response('Unauthorized', { status: 401 })
    }
  })
})

export const config = {
  matcher: ['/((?!_next|.*\\..*).*)'],
}

