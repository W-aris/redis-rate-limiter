# Redis Fixed Window Rate Limiter (POC)

## Overview
This project is a **Proof of Concept (POC)** implementation of a **Redis-based Fixed Window Rate Limiter** written in **Python**.

The rate limiter restricts the number of requests allowed **per IP address and API route** within a fixed time window using Redis counters and key expiration (TTL).

This project focuses on **clarity and correctness**, not production hardening.

---

## Objective
- Track requests per **IP + API route**
- Allow a maximum of **N requests**
- Within a fixed window of **T seconds**
- Block further requests once the limit is exceeded
- Automatically reset after the window expires

---

## Rate Limiting Strategy

### Algorithm Used
**Fixed Window Counter**

- Requests are counted in discrete time windows
- Redis key expiration determines the window boundary
- Once the request count exceeds the limit, all further requests are blocked until the key expires

---
