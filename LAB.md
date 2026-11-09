# Hands-On Lab: Scanning Chainguard Myself

I didn't want to repeat "97.6% fewer CVEs" to a security engineer without testing it first. So I took one common web server, nginx, and ran the standard image and Chainguard's image through the same scanner. Date: November 9, 2026.

## Setup

- A GitHub Codespace on this repo: a Linux machine in the browser with Docker already installed
- Scanner: Grype v0.121.2, a free, independent open source tool
- Images: `nginx:latest` from Docker Hub and `cgr.dev/chainguard/nginx:latest`, which pulled with no login or account

## Results

| | Stock nginx | Chainguard nginx |
|---|---|---|
| Size on disk | 243 MB | 29.4 MB |
| Packages | 153 | 23 |
| Executables | 833 | 32 |
| Files | 3,237 | 107 |
| Scanner matches | 355 | 1 |
| Unique vulnerabilities | 191 | 1 |
| Critical (unique) | 10 | 0 |
| High (unique) | 57 | 1 |
| Medium (unique) | 47 | 0 |
| Low (unique) | 8 | 0 |
| Negligible (unique) | 68 | 0 |
| Unknown (unique) | 1 | 0 |
| Matches with a fix available | 3 of 355 | 0 of 1 |
| Shell at `/bin/sh` | Yes | No (`no such file or directory`) |
| Default user | Not set, so root | 65532 (non-root) |

Then I started the Chainguard image and sent it a request. It answered `HTTP/1.1 200 OK`, so the smaller image still does its job.

## What it taught me

1. The savings come from what's missing. Most of the stock findings sit in packages nginx doesn't need to serve a page. Going from 153 packages to 23 removes the problem instead of tracking it.
2. Patching wouldn't have closed this gap. Only 3 of the 355 stock matches had a fix available. So when a prospect says "we patch base images ourselves," the better question is what they do about the findings that have no patch to apply. Under FedRAMP, those still have to be tracked.
3. A smaller attack surface is the default. With no shell and a non-root user, there's less for an attacker to work with after getting in, and nobody on the customer's team had to configure that.
4. Zero isn't the right promise. Chainguard's image still showed one High. New vulnerabilities will keep appearing in any software, which is why the remediation SLA matters as much as the clean scan.

## What this doesn't prove

This is one image, one scanner, one morning. My result is better than Chainguard's published 97.6% average, but I wouldn't quote it as a benchmark. 68 of the stock findings are rated Negligible (123 remain without them). A real FedRAMP boundary also has the customer's own layers on top, which is why the useful test is their last scan against their own images.

## How I'd explain it to a buyer

"I scanned stock nginx against Chainguard's build this morning. 67 critical and high findings became 1, and almost none of the stock findings had a fix you could apply. Worth running the same comparison on your own images?"

## Commands, for anyone repeating this

```
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo sh -s -- -b /usr/local/bin

docker pull nginx:latest
docker pull cgr.dev/chainguard/nginx:latest
docker images | grep nginx

scan() { grype "$1" -o json | jq -r '.matches[].vulnerability | "\(.severity) \(.id)"' | sort -u | cut -d' ' -f1 | sort | uniq -c; }
scan nginx:latest
scan cgr.dev/chainguard/nginx:latest

docker run --rm --entrypoint /bin/sh nginx:latest -c 'echo stock has a shell'
docker run --rm --entrypoint /bin/sh cgr.dev/chainguard/nginx:latest -c 'echo chainguard has a shell'

docker inspect --format 'stock user=[{{.Config.User}}]' nginx:latest
docker inspect --format 'chainguard user=[{{.Config.User}}]' cgr.dev/chainguard/nginx:latest

docker run -d --name cg -p 8080:8080 cgr.dev/chainguard/nginx:latest
curl -sI localhost:8080 | head -1
docker rm -f cg
```

Sources: [Grype](https://github.com/anchore/grype) · [Getting started with the nginx Chainguard Container](https://www.chainguard.dev/docs/chainguard/containers/getting-started/web-and-data-services/nginx/index.md)
