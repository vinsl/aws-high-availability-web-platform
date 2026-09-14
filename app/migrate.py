from db import get_connection

with get_connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                author VARCHAR(100) NOT NULL,
                title VARCHAR(200) NOT NULL,
                content TEXT NOT NULL,
                status ENUM('open', 'in_progress', 'resolved', 'closed', 'cancelled')
                    NOT NULL DEFAULT 'open',
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

print("Migration completed: tickets table is ready.")