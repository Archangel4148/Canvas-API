# Canvas Course Tool

## Overview
This Python script interacts with the Canvas API to provide course and student information. It allows users to:

- **List the roster of a selected course**
- **Find students who share multiple courses with the user**

## Prerequisites
- **Python 3.x installed**
- **A valid Canvas API Token**
- **The `canvasapi` library installed:**
  ```sh
  pip install canvasapi
  ```

## Setup
### 1. Configure API Credentials
Before running the script, create a `canvas_info.json` file in the project directory. This file should contain:
```json
{
    "canvas_url": "https://your-canvas-instance.com",
    "api_token": "your-api-token-here"
}
```
> **Important:** Do NOT share your API token or commit it to a public repository.

### 2. Run the Script
Execute the script with:
```sh
python script.py
```

## Usage
When you run the script, you will be presented with a menu:

1️⃣ **List a course roster** – Displays all students in a selected course.  
2️⃣ **Find students who share multiple classes with you** – Identifies students who share more than one class with you and lists the courses you share.

