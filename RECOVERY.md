# If git goes wrong: the scripted recovery path

Work down the list. Stop at the first one that fits. Nothing here loses work
that has been committed.

| Symptom | What it means | Do this |
|---|---|---|
| `Updates were rejected ... fetch first` | somebody pushed before you | `git pull --rebase` then `git push` |
| `Please commit your changes or stash them before you switch` | uncommitted edits in the way | `git add -A && git commit -m "wip"` then switch |
| `CONFLICT (content): Merge conflict in X` | two branches changed the same lines | open X, keep what is correct, delete the `<<<<<<<` `=======` `>>>>>>>` lines, `git add X`, `git commit` |
| halfway through a merge and lost | | `git merge --abort` — you are back where you started |
| halfway through a rebase and lost | | `git rebase --abort` |
| committed to the wrong branch | | `git log --oneline -1` (copy the id), `git reset --hard HEAD~1`, `git switch <right-branch>`, `git cherry-pick <id>` |
| committed something that should not be there | not pushed yet | `git reset --soft HEAD~1`, fix, commit again |
| committed something that should not be there | already pushed | `git revert <id>` |
| deleted a branch, reset too far, "lost" a commit | | `git reflog`, find the id, `git switch -c rescue <id>` |
| `Authentication failed` | password instead of a token | `gh auth login`, or use GitHub Desktop |
| no idea what state the repository is in | | `git status` then `git log --oneline --graph --all -20` — read them before typing anything else |

## The last resort, which always works

Your commits are safe on the server once pushed. If your local clone is beyond
saving, rename the folder and clone again:

```bash
cd ..
mv toolbox toolbox-broken
git clone <repository url>
```

Then copy across any file you had not committed. **Do not delete
`toolbox-broken` until the end of the session** — anything you had committed
locally is still in its `.git` folder.

## Ask before you force

`git push --force` on a shared branch deletes other people's work from the
server. If you believe you need it, call a teacher over first.
