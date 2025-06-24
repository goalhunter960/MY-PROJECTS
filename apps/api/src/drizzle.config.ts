import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./apps/api/src/schema.ts",   // ✅ your actual schema location
  out: "./drizzle",                     // Folder where migration SQL will go
  dialect: "postgresql",
  dbCredentials: {
    connectionString: process.env.DATABASE_URL!,
  },
});

