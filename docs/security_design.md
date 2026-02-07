# Security Design Document
## Project: Secure Web Application & Threat Hardening

**Prepared BY:** Manish Suthar
**Role:** BCA Student
**Internship Domain:** Cyber Security & Ethical Hacking
**Organization:** Cryptonic Area
**Submission Date** 8 February 2026

---

### 1. Introduction
This document explains the security design decisions implemented in the project.
The objective is to protect the web application against common web-based attacks
by applying manual and practical security controls.

---

### 2. Architecture Overview
The application follows a modular architecture:
- Flask handles routing and request processing
- SQLite is used for secure data storage
- Separate security modules handle authentication, validation, and sessions

Security logic is isolated from business logic to reduce attack surface.

---

### 3. Authentication Design
- Username and password based authentication
- Passwords are never stored in plaintext
- Bcrypt hashing with salt is used
- Login attempts are validated against stored hashed passwords

Reason:
Hashing ensures credential confidentiality even if database is compromised.

---

### 4. Authorization & Access Control
- Role-based access control (RBAC) implemented
- Default role: user
- Admin-only routes protected via middleware
- Unauthorized users are redirected safely

Reason:
Prevents privilege escalation attacks.

---

### 5. Password Policy
- Minimum length: 8 characters
- Must include uppercase, lowercase, and special character
- Common weak passwords rejected

Reason:
Reduces risk of brute-force and credential stuffing attacks.

---

### 6. Input Validation & Sanitization
- Server-side validation implemented for all user inputs
- Dangerous characters (< > ' ") are sanitized
- Regex-based username validation applied

Reason:
Prevents XSS and injection attacks.

---

### 7. Session Management
- Flask-Login used for secure session handling
- Session timeout enforced via configuration
- Session cookies are protected by secret keys

Reason:
Prevents session fixation and hijacking.

---

### 8. Logging & Monitoring
- Login and access events logged
- Suspicious activities can be reviewed from logs directory

Reason:
Helps in detecting security incidents.

---

### 9. Conclusion
The security design follows OWASP recommended practices and focuses on
manual implementation rather than third-party automation.