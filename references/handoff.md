# Verifiable handoff protocol

1. Confirm scope, permission and canonical project.
2. Record repository, branch and commit **only when independently observed**.
3. Separate implemented, documented, tested, deployed and published.
4. For each test, record command, environment, result, time and primary evidence. Include skipped/not_run.
5. Record decisions, rejected alternatives, risks, blockers and next exact action.
6. Incoming agent first verifies repository and evidence, flags mismatches and continues only within authorized scope.

Required concepts: project_id, prepared_at, scope, permissions, repository/ref, verified facts, test outcomes, blockers, next action, supporting evidence, unverified claims.

A handoff is not independent proof that code exists, a test ran, or a release was published.
