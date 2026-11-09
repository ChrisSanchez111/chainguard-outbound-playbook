# Hands-On Lab: Running Chainguard Myself

I wanted to test Chainguard's claims before pitching them to security engineers. I scanned the standard nginx image and Chainguard's nginx image with the same tool and compared the results. Date: November 9, 2026.

## Setup

I ran this in a GitHub Codespace on this repo, which comes with Docker installed.

- Scanner: Grype v0.121.2, a free open source tool from Anchore
- Images: `nginx:latest` from Docker Hub and `cgr.dev/chainguard/nginx:latest`
- The Chainguard image pulled without a login

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

I then started the Chainguard image and sent it a request. It returned `HTTP/1.1 200 OK`.

## What I learned

1. Chainguard's image has 23 packages to stock's 153, and it's 88% smaller. Fewer packages meant fewer findings.
2. Only 3 of the 355 stock matches showed a fix available. If a prospect says "we patch base images ourselves," I'd ask what they do about the findings with no patch.
3. Chainguard's image has no shell and doesn't run as root by default.
4. Chainguard's image still had one High. I'd talk about the SLA along with the scan results.

## Limits

I only tested one image, so I wouldn't quote this as a benchmark. It came out better than Chainguard's published 97.6% average. 68 of the stock findings are rated Negligible. A customer's images also have their own code on top, so the real test is a scan of their images.

## How I'd explain it to a buyer

"I scanned stock nginx and Chainguard's nginx. Stock had 67 critical and high findings. Chainguard's had 1. Can we run the same comparison on your images?"

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
