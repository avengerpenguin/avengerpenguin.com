Title: Continuous Delivery with Microservices

# Test Strategy

Test pyramid applies pre-prod

In prod:

* Monitoring, tracing, fault-injection testing
* Canary deployments, Blue-Green deployments, A/B Testing

Fault Injection e.g. Simian Army

# CI

* Feature toggles

# Environments

* Environment plan with intended use
* Dynamic environment creation

Repo -> CI -> (Showcase, Dev) -> Promote -> (QA, Perf) -> Promote ->
(Prod, DR)

# Managing Configuration

# Remediation

* Roll forward
* Rollback
* Hotfix pipeline deploys straight to production
