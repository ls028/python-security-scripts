# Python Security Scripts

A collection of Python scripts for security automation, network analysis, and cybersecurity tooling. Built as part of my journey toward CompTIA A+, Network+, and Security+ certifications and a career as a SOC Analyst.

---

## Repository Structure

```
python-security-scripts/
├── network/
│   └── port_scanner.py          # TCP port scanner with service identification
├── password-tools/
│   └── password_generator.py    # Secure password generator with custom options
├── log-analysis/
│   └── (coming soon)
└── automation/
    └── (coming soon)
```

---

## Scripts

### 🔍 Network / port_scanner.py
Scans a target IP or hostname for open TCP ports and identifies the running service.

**Usage:**
```bash
python port_scanner.py
```
**Features:**
- Scans 11 common ports (FTP, SSH, HTTP, HTTPS, RDP, MySQL, DNS, and more)
- Identifies service name for each open port
- 1-second timeout per port for fast scanning
- Handles hostname resolution errors gracefully

**Example output:**
```
Scanning 192.168.1.254...

Port 53: OPEN (DNS)
Port 80: OPEN (HTTP)
Port 443: OPEN (HTTPS)

Scan complete. 3 open port(s) found.
```

---

### 🔐 Password Tools / password_generator.py
Generates cryptographically random passwords with configurable length and character sets.

**Usage:**
```bash
python password_generator.py
```
**Features:**
- Configurable password length
- Optional symbol inclusion
- Generates 5 password options per run
- Uses Python's `random.choices()` for unpredictable output

---

## Skills Demonstrated

- Python scripting for security automation
- TCP socket programming and network connectivity testing
- Port enumeration and service identification
- Secure random password generation
- Error handling and exception management

---

## Certifications In Progress

- ✅ CompTIA A+ Core 1 (220-1201) — studying
- 🔄 CompTIA Network+ — after A+
- 🔄 CompTIA Security+ — after Network+

---

## Related Repositories

- [packet-tracer-labs](https://github.com/ls028/packet-tracer-labs) — Cisco Packet Tracer network labs
- [TryHackMe](https://github.com/ls028/TryHackMe) — SOC Level 1 learning path progress

---

*Building toward SOC Analyst / Junior Security Analyst roles. AA Mathematics @ Miami Dade College. BS Cybersecurity (in progress).*
