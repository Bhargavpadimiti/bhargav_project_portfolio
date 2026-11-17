# Git cheat sheet

The commands that cover 95% of day-to-day work in this repo.

## Daily loop

| Task | Command |
| ---- | ------- |
| What changed? | `git status` / `git diff` |
| Stage everything | `git add -A` |
| Stage part of a file | `git add -p` |
| Commit (opens the message template) | `git commit` |
| Quick one-line commit | `git commit -m "fix(weather-cli): handle empty city"` |
| Push the current branch | `git push` |
| Get the latest changes | `git pull` |

## Branches

| Task | Command |
| ---- | ------- |
| New branch from here | `git switch -c feat/my-feature` |
| Switch branch | `git switch main` |
| List branches | `git branch -vv` |
| Delete a merged branch | `git branch -d feat/my-feature` |
| Update my branch with latest main | `git fetch && git rebase origin/main` |

## Pull requests with the GitHub CLI

| Task | Command |
| ---- | ------- |
| Open a PR from this branch | `gh pr create --fill` |
| See PR checks (CI) | `gh pr checks --watch` |
| Open the PR in the browser | `gh pr view --web` |
| Merge and clean up | `gh pr merge --squash --delete-branch` |
| Check out someone's PR | `gh pr checkout 12` |
| Create an issue | `gh issue create` |

## Undo things

| Oops… | Fix |
| ----- | --- |
| Discard changes to a file | `git restore path/to/file` |
| Unstage a file | `git restore --staged path/to/file` |
| Fix the last commit message | `git commit --amend` |
| Add a forgotten file to the last commit | `git add file && git commit --amend --no-edit` |
| Undo the last commit, keep the changes | `git reset --soft HEAD~1` |
| Undo a commit that's already pushed | `git revert <sha>` (makes a new "undo" commit) |
| Committed to `main` by mistake | `git branch feat/x && git reset --keep origin/main && git switch feat/x` |
| Find a "lost" commit | `git reflog` |

## Look around

| Task | Command |
| ---- | ------- |
| Compact history graph | `git log --oneline --graph --decorate -20` |
| History of one project | `git log --oneline -- projects/weather-cli` |
| Who changed this line? | `git blame path/to/file` |
| Find which commit broke something | `git bisect start` → `git bisect bad` → `git bisect good <sha>` |

## Park work for later

| Task | Command |
| ---- | ------- |
| Stash changes | `git stash push -m "wip: forecast parsing"` |
| List stashes | `git stash list` |
| Restore the latest stash | `git stash pop` |

## Hooks

| Task | Command |
| ---- | ------- |
| Run all checks now | `pre-commit run --all-files` (or `make lint`) |
| Update hook versions | `pre-commit autoupdate` |
| Skip hooks once (emergency only) | `git commit --no-verify` |

## Handy aliases (optional, global)

```bash
git config --global alias.st "status -sb"
git config --global alias.lg "log --oneline --graph --decorate -20"
git config --global alias.undo "reset --soft HEAD~1"
git config --global alias.sync '!git switch main && git pull --prune && git branch -vv | awk "/: gone]/{print \$1}" | xargs -r git branch -D'
```

After that, `git sync` returns to `main`, pulls, and deletes local branches whose
pull request was merged (their GitHub branch is gone).
