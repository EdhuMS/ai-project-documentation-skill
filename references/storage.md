# Storage contract

- Local Markdown/JSON is the portable core. Git and external storage are optional.
- Identify each destination's actual read/list/write/version/export capabilities and permissions. Never assume cloud access.
- Assign one canonical home per artifact; mirrors should record source revision/hash. Git commits and cloud revision IDs are not interchangeable.
- On divergence: compare, preserve both, report conflict, obtain resolution, write only after authorization, and verify readback.
- Example canonical local path: `./docs/continuity/`; Git path: `docs/continuity/`. External folder IDs must be verified, not invented.
- Unsupported actions: provide portable files for manual transfer. Never imply that a mirror was synchronized if it was not.
