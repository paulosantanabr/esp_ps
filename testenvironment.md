# 🧪 Simple Lab Setup for Checkmk Extension Development

This guide explains how to set up a lightweight environment to test and develop Checkmk extensions using **Docker Desktop** and **Cursor with Claude 3.5** — no terminal commands required.

---

## 🚀 Step 1: Run Checkmk via Docker Desktop GUI

1. Open **Docker Desktop**.
2. Click **"Create"** > **"Create Container"**.
3. In the image selector, search for:  
   - `checkmk/check-mk-cloud:2.2.0-latest` or  
   - `checkmk/check-mk-raw:2.2.0-latest`
4. In the **Ports** section, set both ports to `0`  
   *(this allows Docker to assign random available ports)*
5. Click **Create & Run**.

---

## 🧑‍💻 Step 2: Use Cursor with Dev Containers + Claude 3.5

1. Install **Cursor** from [https://cursor.sh](https://cursor.sh)
2. Make sure **Dev Containers** extension is enabled.
3. Open Cursor and attach to the running Checkmk container.
4. Inside the container, mount the plugin path:
   ```
   /omd/sites/cmk/local/lib/python3/cmk_addons/plugins
   ```
5. Use the default site user:  
   - **Username:** `cmk`

---

## ✅ Done!

You’re now set up to:
- Run Checkmk from Docker
- Use AI-assisted development with Claude 3.5 in Cursor
- Write and test plugins in the actual Checkmk environment

---

🛠️ *Quick Tip:*  
Use the Checkmk GUI in your browser by checking the port mapped in Docker Desktop → click the container → “Open in browser.”
