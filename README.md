# Multi-Agent AI Task Manager

## Overview
This project is a simple Multi-Agent AI system that helps users manage tasks, schedules, and notes using a centralized main agent.

The system demonstrates how multiple agents (tools) can work together to handle different types of user requests efficiently.

---

## Features
- Task management
- Event scheduling
- Note storage
- Simple memory tracking
- Command-line interaction

---

## Architecture

Main Agent (Controller):
- Receives user input
- Decides which tool to use

Tools (Simulated MCP Integration):
- Task Tool → Handles task-related requests
- Calendar Tool → Manages scheduling
- Notes Tool → Stores notes

The system simulates Model Context Protocol (MCP) by allowing the main agent to interact with different tools.

---

## How It Works
1. User enters a request
2. Main Agent processes the input
3. Based on keywords, the request is routed to the appropriate tool
4. Tool processes the request and returns a response
5. Response is stored in memory and displayed

---

## Example Usage

Input:
Add task: complete project

Output:
[Task Tool] Task added: add task: complete project

Input:
Schedule meeting tomorrow

Output:
[Calendar Tool] Event scheduled: schedule meeting tomorrow

Input:
Take note: learn AI

Output:
[Notes Tool] Note saved: take note: learn ai

---

## Technologies Used
- Python

---

## Future Improvements
- Web-based interface
- Integration with real APIs (Google Calendar, Notion, etc.)
- Deployment using Google Cloud Run
- Enhanced NLP for better understanding

---

## Note
This project demonstrates the concept of a multi-agent system with simulated MCP integration.  
Due to time constraints, real-world API integrations and cloud deployment are planned for future development.

---

## Author
Azar Abdullah
