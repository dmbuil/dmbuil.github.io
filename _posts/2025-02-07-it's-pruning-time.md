---
date: 2025-02-07 23:24:44
layout: post
title: "It's pruning time"
subtitle: Prune obsolete local branches in Git
description: Learn how to prune obsolete local branches in Git with a simple snippet.
image: 
  path: https://res.cloudinary.com/dguibifnv/image/upload/t_crop_and_save/v1744149288/dmbuil-github-pages/pruth2.jpg
  lqip: https://res.cloudinary.com/dguibifnv/image/upload/t_to_thumbnail/v1744149288/dmbuil-github-pages/pruth2.jpg
category: snippets
tags: 
 - git
author: dmbuil
paginate: false
---

When working with Git, especially on collaborative projects, it's easy to accumulate obsolete local
branches that no longer serve any purpose.  
These lingering branches can clutter your repository, make navigation cumbersome, and even lead to confusion when trying to recall the project's history. 

In this little post, I'll walk through a powerful yet somewhat complex snippet I came up with to help purge these unnecessary local branches.

## The Command, Unveiled

The command in question is:

```bash
git fetch -p ; git branch -r | awk '{print $1}' | egrep -v -f /dev/fd/0 <(git branch -vv | grep origin) | awk
'{print $1}' | xargs git branch -d
```

At first glance, this command appears daunting with its numerous pipes and options. However, upon dissecting it
step by step, you'll find that each component plays a specific role in achieving the goal of cleaning up obsolete
branches.

## Step-by-Step Breakdown

1. **Fetch and Prune (`git fetch -p`)**:
   - This command updates your local repository with the latest changes from the remote (e.g., GitHub, GitLab)
and removes any local references to branches that have been deleted on the remote. It's like spring cleaning for
your local repository, ensuring you don't keep unnecessary references lying around.

2. **List Remote Branches (`git branch -r | awk '{print $1}'`)**:
   - The `-r` flag in `git branch` lists all branches available on the remote. By appending `| awk '{print $1}'`,
we extract just the branch names, creating a list of all active remote branches.

3. **Identify Active Local Branches (`git branch -vv | grep origin`)**:
   - Using `git branch -vv`, you retrieve a detailed list of all local branches along with their tracking
information. The `grep origin` filters this list to show only those branches that track the "origin" remote,
which are typically your main and feature branches.

4. **Exclude Active Branches (`egrep -v -f /dev/fd/0 <(...)`)**:
   - The `egrep -v -f` command is used here to exclude patterns from a list. In this context, it excludes any
branch names that are still being tracked by the origin remote, ensuring only obsolete branches remain.

5. **Delete Obsolete Branches (`awk '{print $1}' | xargs git branch -d`)**:
   - Finally, the remaining branch names (those not excluded) are passed to `xargs git branch -d`, which deletes
each of these branches from your local repository.

## Why This Matters

Cleaning up obsolete local branches is essential for several reasons:

- **Clarity**: A cluttered list of branches can obscure the project's actual state, making it harder to focus on
active work.
- **Efficiency**: Keeping unnecessary branches around consumes disk space and can slow down certain Git
operations.
- **Collaboration**: When working in a team, obsolete branches that linger can confuse other developers about
what's current or relevant.

> **Danger Zone**  
> While this command is powerful, it's crucial to use it judiciously. 
> Deleting branches can't be undone easily, so ensure you have backed up any critical work and double-check the list of branches to be deleted before executing the command.
{: .prompt-danger }
