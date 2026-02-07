# Threat Modeling Document
## Project: Secure Web Application & Threat Hardening

**Prepared BY:** Manish Suthar
**Role:** BCA Student
**Internship Domain:** Cyber Security & Ethical Hacking
**Organization:** Cryptonic Area
**Submission Date** 8 February 2026

---

### 1. Objective
The objective of this threat model is to identify possible threats,
analyze their impact, and apply appropriate mitigation strategies.

---

### 2. Assets Identified
- User credentials
- Session tokens
- Application database
- Application availability

---

### 3. Threat Identification

| Threat | Description |
|------|------------|
| SQL Injection | Malicious input targeting database queries |
| XSS | Injection of malicious scripts via user input |
| Brute Force | Multiple login attempts using weak passwords |
| Session Hijacking | Stealing active user sessions |
| Privilege Escalation | Gaining unauthorized admin access |

---

### 4. Risk Analysis

| Threat | Risk Level |
|------|-----------|
| SQL Injection | Medium |
| XSS | Medium |
| Brute Force | High |
| Session Hijacking | High |
| Privilege Escalation | Medium |

---

### 5. Mitigation Strategies

| Threat | Mitigation |
|------|-----------|
| SQL Injection | Parameterized queries |
| XSS | Input sanitization and validation |
| Brute Force | Strong password policy |
| Session Hijacking | Secure session handling |
| Privilege Escalation | Role-based access control |

---

### 6. Residual Risks
- No CAPTCHA implemented
- No account lockout after multiple failures
These are documented as future improvements.

---

### 7. Conclusion
Threat modeling helped in identifying realistic attack scenarios
and implementing appropriate security controls early in development.