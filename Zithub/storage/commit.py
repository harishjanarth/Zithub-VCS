from datetime import datetime
class commitNode:
    def __init__(self, message, timestamp, file_changes=None):
        self.message = message
        self.timestamp = timestamp
        self.file_changes = file_changes if file_changes else []
        self.next = None

class commitHistory:
    def __init__(self):
        self.head = None

    def add_commit(self, message, file_changes=None):
        new_commit = commitNode(message=message, timestamp=datetime.utcnow(), file_changes=file_changes)

        if not self.head:
            # If no commits exist, set the new commit as the head
            self.head = new_commit
        else:
            # Traverse to the end of the list and add the new commit
            current = self.head
            while current.next:
                current = current.next
            current.next = new_commit
        print(f"Commit added: {message}, Timestamp: {new_commit.timestamp}")
