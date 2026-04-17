# Day 12 Lab - Mission Answers

## Part 1: Localhost vs Production

### Exercise 1.1: Anti-patterns found
1. **Hardcoded Secrets & Config:** API keys, database URLs, and settings like `DEBUG=True` are written directly in the code. This is a major security risk and makes configuration inflexible.
2. **Using `print` for Logging:** `print()` is used instead of a structured logger, making logs hard to parse, filter, and analyze. It also logs sensitive data.
3. **No Health Check Endpoint:** There's no `/health` or similar endpoint for orchestration platforms (like Kubernetes) to verify if the application is alive and ready to serve traffic.
4. **Hardcoded Host/Port:** The server binds to `localhost:8000`, which won't work inside a container or on most cloud platforms that require binding to `0.0.0.0` and a dynamic port.
5. **Debug Mode in Production:** `reload=True` is enabled, which is inefficient and insecure for a production environment.

### Exercise 1.3: Comparison table
| Feature | Develop | Production | Why Important? |
|---------|---------|------------|----------------|
| **Config** | Hardcoded in `app.py` | Loaded from environment variables via `config.py` | **Portability & Security:** Allows the same app to run in different environments (dev, prod) without code changes. Prevents secrets from being committed to version control. (12-Factor App: III. Config) |
| **Secrets** | Hardcoded string (`sk-hard...`) | Loaded via `os.getenv("OPENAI_API_KEY")` | **Security:** Avoids leaking credentials. Keys can be managed securely by the deployment platform. |
| **Logging** | `print()` statements | Structured JSON logging | **Observability:** JSON logs can be easily ingested, searched, and analyzed by log management systems (like Datadog, Splunk, Loki). |
| **Server Binding** | `localhost:8000` | `0.0.0.0:$PORT` | **Deployability:** `0.0.0.0` is required to be accessible from outside a container. Dynamic `$PORT` is necessary for PaaS platforms like Railway or Render. |
| **Health Check** | None | `GET /health` endpoint | **Reliability:** Allows automated systems to detect a failing application and restart it, ensuring high availability. |
| **Shutdown** | Abrupt (Ctrl+C) | Graceful (handles `SIGTERM`) | **Data Integrity & Reliability:** Ensures in-flight requests are completed before the app shuts down, preventing data loss and client errors. |

## Part 2: Docker

### Exercise 2.1: Dockerfile questions
1.  **Base image (`develop`):** `python:3.11`. This is a full Python image, including build tools.
2.  **Working directory (`develop`):** `/app`. This is the directory inside the container where commands will run.
3.  **Base image (`production`):** `python:3.11-slim`. The multi-stage build uses the smaller `-slim` variant for both the `builder` and final `runtime` stages to create a smaller, more secure final image.
4.  **Non-root user (`production`):** `appuser`. The production Dockerfile creates and switches to a non-root user, which is a critical security best practice to limit potential container breakouts.

### Exercise 2.3: Image size comparison
- **Develop:** 1.12 GB
- **Production:** 204.38 MB
- **Difference:** The production image is **~81.8% smaller**. This significant reduction is achieved by using a multi-stage build, a slimmer base image, and not including build-time dependencies in the final image.
### Exercise 3.1: Railway deployment
- URL: https://laudable-achievement-production-f251.up.railway.app
- Screenshot: railwaydeploy.png

## Part 4: API Security

### Exercise 4.1-4.3: Test results
[Paste your test outputs]

### Exercise 4.4: Cost guard implementation
[Explain your approach]

## Part 5: Scaling & Reliability

### Exercise 5.1-5.5: Implementation notes
[Your explanations and test results]