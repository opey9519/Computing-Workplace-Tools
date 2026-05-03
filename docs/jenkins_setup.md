# Jenkins Setup Guide

Jenkins must be able to run `docker` and `docker compose` commands during the pipeline.
The official `jenkins/jenkins:lts` image does not include the Docker CLI, so this project
uses a custom image that adds Docker CLI and Python 3.

---

## Why a Custom Image Is Needed

When Jenkins runs inside a Docker container it has no access to the host Docker daemon by
default. The fix is two parts:

1. Install the Docker CLI inside the Jenkins image.
2. Mount the host Docker socket into the container so the CLI can reach the daemon.

---

## Step 1 — Build the Custom Jenkins Image

Run this from the **repo root** (where `Dockerfile.jenkins` lives):

```bash
docker build -t jenkins-with-docker -f Dockerfile.jenkins .
```

---

## Step 2 — Stop and Remove the Old Jenkins Container

If a plain `jenkins/jenkins:lts` container is already running, stop and remove it first.
The volume (`jenkins_home`) is kept so your job configuration is preserved.

```bash
docker stop jenkins || true
docker rm jenkins || true
```

---

## Step 3 — Start the New Jenkins Container

> **Windows / Git Bash:** Git Bash converts `/var/run/docker.sock` to a Windows path,
> which causes the container to fail with `Access is denied`. Prefix the command with
> `MSYS_NO_PATHCONV=1` to disable that conversion.

```bash
MSYS_NO_PATHCONV=1 docker run -d \
  --name jenkins \
  --user root \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins-with-docker
```

- `--user root` ensures Jenkins has permission to access the mounted Docker socket.
- `-v /var/run/docker.sock:/var/run/docker.sock` gives the Jenkins pipeline access to the
  host Docker daemon so it can run `docker build` and `docker compose`.

---

## Step 4 — Verify the Container Has Docker, Docker Compose, and Python

```bash
docker exec jenkins docker --version
docker exec jenkins docker compose version
docker exec jenkins python3 --version
```

All three commands should print version strings. If any fail, the image did not build
correctly — re-run Step 1.

---

## Step 5 — Open Jenkins and Run the Pipeline

1. Open `http://localhost:8080`.
2. If this is a fresh container, retrieve the unlock password:
   ```bash
   docker logs jenkins 2>&1 | grep -A 2 "Please use the following password"
   ```
3. Follow the setup wizard (install suggested plugins, create admin user).
4. Create a **Pipeline** job:
   - **Definition:** Pipeline script from SCM
   - **SCM:** Git
   - **Repository URL:** your GitHub repo URL
   - **Branch Specifier:** `*/main`
   - **Script Path:** `Jenkinsfile`
5. Click **Save**, then **Build Now**.

---

## Troubleshooting: Issues we found during setup and testing

### `docker: not found` (exit code 127)

**Meaning:** The Jenkins container is running the plain `jenkins/jenkins:lts` image which
does not include the Docker CLI.

**Fix:** Follow Steps 1–3 above to rebuild with `Dockerfile.jenkins` and restart the
container with the socket mounted.

---

### `permission denied` on `/var/run/docker.sock`

**Meaning:** The Jenkins process inside the container does not have permission to access
the mounted Docker socket.

**Fix:** Start the container with `--user root` as shown in Step 3. This is the reliable
solution for a local/class demo environment.

If the container is already running without `--user root`, stop and remove it, then
restart it with the correct flags (Step 2 → Step 3).

---

### `unknown shorthand flag: 'f' in -f` during Deploy

**Meaning:** The `docker compose` subcommand is not recognized. Jenkins is passing `-f`
directly to the `docker` CLI, which does not accept that flag — meaning `compose` is not
installed as a Docker CLI plugin inside the Jenkins container.

**Fix:** Rebuild the Jenkins image using `Dockerfile.jenkins` (Step 1). The Dockerfile
installs Docker Compose v2 as a CLI plugin so `docker compose` works as a subcommand.

---

### `fatal: not in a git directory` during Checkout

**Meaning:** The Jenkins workspace is stale or corrupted from a previous failed build.
Jenkins detects a `.git` folder remnant but it is incomplete, so `git config` fails.

**Fix — clean the workspace folders from outside the container:**

On Windows (Git Bash), `docker exec -it` requires `winpty`. Use the non-interactive form instead:

```bash
docker exec jenkins rm -rf /var/jenkins_home/workspace/ci-cd-notification-system
docker exec jenkins rm -rf "/var/jenkins_home/workspace/ci-cd-notification-system@tmp"
docker exec jenkins rm -rf "/var/jenkins_home/workspace/ci-cd-notification-system@script"
```

Then go back to Jenkins and click **Build Now**.

The Jenkinsfile also includes `skipDefaultCheckout(true)` and `deleteDir()` at the start
of the Checkout stage, which prevents this from recurring on future builds.

---

### `docker exec -it` fails with "not a TTY" (Windows/Git Bash)

**Meaning:** Git Bash (mintty) does not allocate a TTY, so `-it` fails.

**Fix:** Prefix with `winpty`:

```bash
winpty docker exec -it jenkins bash
```

Or drop the interactive flags and run commands directly:

```bash
docker exec jenkins <command>
```

---
