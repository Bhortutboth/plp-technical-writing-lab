# Technical Writing Lab Assignment

## Exercise A: User Manual Procedure

### Title: How to Create a GitHub Repository and Make Your First Commit

### 1. Purpose

This procedure explains how to create a new GitHub repository, connect it to a local computer, and save the first version of a project using Git. It is intended for first-semester computing students who have basic computer skills but are new to Git and GitHub.

### 2. Prerequisites

Before starting, the reader needs:

* A computer running Windows, macOS, or Linux.
* A working internet connection.
* A GitHub account.
* Git installed on the computer.
* A code editor, such as Visual Studio Code.
* Basic knowledge of opening a terminal or Git Bash.

### 3. Procedure

**Step 1: Sign in to GitHub.**

Action: Open https://github.com and sign in to your account.

Expected result: Your GitHub dashboard appears.

**Step 2: Open the repository creation page.**

Action: Click the plus (+) icon in the top-right corner and select **New repository**.

Expected result: The new repository form appears.

**Step 3: Enter a repository name.**

Action: Type `my-first-project` in the repository name field.

Expected result: The repository name appears in the form.

**Step 4: Create the repository.**

Action: Click **Create repository**.

Expected result: GitHub displays the new repository page with its URL.

**Step 5: Create a local project folder.**

Action: Create a folder named `my-first-project` on your computer.

Expected result: The folder appears in the selected location.

**Step 6: Open the project folder in Git Bash.**

Action: Open Git Bash in the `my-first-project` folder.

Expected result: A terminal opens with the project folder as its working directory.

**Step 7: Initialize Git.**

Action: Run `git init`.

Expected result: Git initializes a repository in the folder.

**Step 8: Create a project file.**

Action: Create a file named `README.md` containing a short description of your project.

Expected result: The README file appears inside the project folder.

**Step 9: Stage the project file.**

Action: Run `git add README.md`.

Expected result: Git stages the README file for the next commit.

**Step 10: Create the first commit.**

Action: Run `git commit -m "Initial commit"`.

Expected result: Git records the first snapshot of your project. If Git requests your identity, configure your name and email before repeating this step.

**Step 11: Connect the local repository to GitHub.**

Action: Run the following command, replacing `YOUR-USERNAME` with your GitHub username:

`git remote add origin https://github.com/YOUR-USERNAME/my-first-project.git`

Expected result: The local repository has a remote named `origin`.

**Step 12: Rename the current branch.**

Action: Run `git branch -M main`.

Expected result: Your current branch is named `main`.

**Step 13: Upload the commit.**

Action: Run `git push -u origin main`.

Expected result: Git uploads your commit to GitHub, and the README file becomes visible on the repository page.

### 4. Screenshot Description

**Screenshot 1: GitHub repository after the first push**

The screenshot should show the GitHub repository page in a web browser. It should display the repository name `my-first-project`, the `main` branch, the `README.md` file, and the initial commit. This screenshot provides evidence that the repository was created and the first commit was uploaded successfully.

### 5. Troubleshooting

**Problem: Git reports that the remote repository could not be found.**

This commonly happens when the remote URL is incorrect or the repository has not been created under the expected GitHub account.

**Solution:**

1. Open the repository page on GitHub.
2. Copy its HTTPS URL.
3. Run `git remote -v` to inspect the current remote URL.
4. If the URL is incorrect, run:

`git remote set-url origin https://github.com/YOUR-USERNAME/my-first-project.git`

5. Retry the push using `git push -u origin main`.

If Git asks for authentication, complete the supported GitHub sign-in process.

### 6. Conclusion

Following these steps enables a beginner to create a GitHub repository, initialize Git locally, make a first commit, and upload the project to GitHub. Git and GitHub help developers track changes, collaborate with others, and maintain a history of their work.

---

## Exercise B: API Reference Entry

### Title: Create a New Project Task API

### 1. Overview

The Create Task API allows an authenticated user to create a new task within an existing project management application. The user provides a task title, an optional description, an assignee, a due date, and a priority level.

The API validates the submitted information, saves the task, and returns the newly created task with its unique ID and other details.

### 2. Endpoint Details

| Property            | Value                                |
| ------------------- | ------------------------------------ |
| HTTP method         | `POST`                               |
| Endpoint path       | `/api/v1/projects/{projectId}/tasks` |
| Content type        | `application/json`                   |
| Authentication      | Bearer token                         |
| Successful response | `201 Created`                        |

### 3. Request Parameters

#### Path parameter

| Name        | Data type | Required | Description                                                         |
| ----------- | --------- | -------- | ------------------------------------------------------------------- |
| `projectId` | String    | Yes      | Unique identifier of the project in which the task will be created. |

There are no query parameters for this endpoint.

#### Request body parameters

| Name          | Data type     | Required | Description                                                                                           |
| ------------- | ------------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `title`       | String        | Yes      | Short title describing the task. Must contain 1–200 characters after trimming whitespace.             |
| `description` | String        | No       | Additional details about the task. May be omitted or set to `null`. Maximum length: 5,000 characters. |
| `assigneeId`  | String        | Yes      | Unique identifier of the user assigned to the task. The user must be eligible to access the project.  |
| `dueDate`     | String (date) | Yes      | Due date in ISO 8601 calendar-date format: `YYYY-MM-DD`.                                              |
| `priority`    | String (enum) | Yes      | Task priority. Accepted values are `low`, `medium`, and `high`.                                       |

### 4. Required Request Headers

| Header          | Required | Description                                                                           |
| --------------- | -------- | ------------------------------------------------------------------------------------- |
| `Authorization` | Yes      | Contains the access token in the format `Bearer YOUR_ACCESS_TOKEN`.                   |
| `Content-Type`  | Yes      | Must be `application/json`.                                                           |
| `Accept`        | No       | Can be set to `application/json` to indicate that the client expects a JSON response. |

### 5. Example Request

**HTTP request**

```http
POST /api/v1/projects/proj_1001/tasks HTTP/1.1
Host: api.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.example
Content-Type: application/json
Accept: application/json
```

**Request body**

```json
{
  "title": "Complete project documentation",
  "description": "Write and review the technical documentation.",
  "assigneeId": "usr_204",
  "dueDate": "2026-10-20",
  "priority": "high"
}
```

### 6. Successful Response

**HTTP status:** `201 Created`

The server returns this status when the task has been validated and created successfully.

**Response body**

```json
{
  "id": "task_5001",
  "projectId": "proj_1001",
  "title": "Complete project documentation",
  "description": "Write and review the technical documentation.",
  "assigneeId": "usr_204",
  "dueDate": "2026-10-20",
  "priority": "high",
  "status": "open",
  "createdBy": "usr_101",
  "createdAt": "2026-10-09T12:30:00Z",
  "updatedAt": "2026-10-09T12:30:00Z"
}
```

The response includes a unique task ID, the submitted task details, the initial status, the ID of the authenticated user who created the task, and timestamps. The sample IDs and timestamp are illustrative.

### 7. HTTP Response Codes

The following table defines the possible responses for this API design.

| Status code                  | Meaning                                            | When it occurs                                                                                                       |
| ---------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `201 Created`                | Task created successfully.                         | The task is validated and saved.                                                                                     |
| `400 Bad Request`            | Invalid request.                                   | The JSON is malformed, a required field is missing, or a field has an invalid format or value.                       |
| `401 Unauthorized`           | Authentication required or invalid.                | The access token is missing, invalid, or expired.                                                                    |
| `403 Forbidden`              | Access denied.                                     | The authenticated user does not have permission to create tasks in the project.                                      |
| `404 Not Found`              | Resource not found.                                | The specified project or assignee does not exist or cannot be found within the applicable access rules.              |
| `409 Conflict`               | Request conflicts with the current resource state. | A project is archived or otherwise cannot accept new tasks.                                                          |
| `415 Unsupported Media Type` | Unsupported request format.                        | The request body is not sent as `application/json`.                                                                  |
| `422 Unprocessable Content`  | Request cannot be processed.                       | The fields are syntactically valid, but a business rule fails, such as assigning a user who is not a project member. |
| `429 Too Many Requests`      | Rate limit exceeded.                               | The client sends requests faster than the API allows.                                                                |
| `500 Internal Server Error`  | Unexpected server error.                           | The server encounters an unhandled error while processing the request.                                               |

These codes form the defined response set for this hypothetical API. A production implementation should use consistent error response bodies and avoid exposing sensitive internal information.

### 8. Example Error Response

**HTTP status:** `400 Bad Request`

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request contains invalid fields.",
    "details": [
      {
        "field": "priority",
        "message": "Priority must be low, medium, or high."
      }
    ]
  }
}
```

The error response identifies the problem and explains which field must be corrected.

### 9. Validation and Behaviour Rules

* The request must be authenticated before a task can be created.
* The project must exist and allow new tasks.
* The title, assignee ID, due date, and priority are required.
* The due date must be a valid calendar date in `YYYY-MM-DD` format.
* The priority must be `low`, `medium`, or `high`, using lowercase values.
* The assignee must be permitted to access the project.
* The server generates the task ID, creation timestamp, update timestamp, and initial status.
* The API does not allow the client to set server-managed fields such as `id`, `status`, or `createdAt` in the request body.

### 10. Conclusion

The Create Task API provides a structured way to add tasks to a project management application. It defines the required inputs, authentication requirements, successful response format, validation rules, and error codes. Clear API documentation helps developers integrate the endpoint correctly and handle errors consistently.
