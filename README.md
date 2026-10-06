# FrameTrace

A multi-vendor DVR/NVR forensic analysis prototype (Smart India Hackathon). One workflow to acquire, identify, parse, recover, correlate and report surveillance evidence from many recorder brands.

## Run locally
```
python run_local.py
```
Opens http://localhost:8000/index.html. Python 3 only, no packages. You can also open `index.html` directly in Chrome.

## What is in this repo
| Path | Purpose |
|---|---|
| `index.html` | The FrameTrace app (single file, works offline) |
| `walkthrough.html` | Animated walkthrough of how it works and how it was built |
| `run_local.py` | One-command local server |
| `docs/architecture-sop.md` | Architecture diagram (Mermaid) and Standard Operating Procedure |
| `docs/case-studies.md` | Public cases and research that motivate the tool |

## What is real and what is simulated
- Real: read-only file intake, MD5 and SHA-256 hashing (first 128 MB in the browser), signature scan for Hikvision and Dahua families, hash-chained custody log, hash re-verification, printable report.
- Simulated in the demo: the recording index, timeline, recovered segments and AI detections.
- Beta: Uniview, TP-Link, Godrej and Matrix use generic H.264/H.265 carving until vendor parsers are built from lab reference images.

## Roadmap
1. Vendor file-system parsers validated on reference images.
2. Real face, object and motion detection on decoded video.
3. Full-disk acquisition agent.
4. Validation reports on real recorders.

## Deploy on GitHub Pages
Settings > Pages > Deploy from a branch > `main` / root. The app is then served at `https://<your-username>.github.io/<repo-name>/`.
