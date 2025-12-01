def store_goal(user_id: str, goal: str):
    return {"status": "stored", "message": f"Goal saved for {user_id}: {goal}"}
