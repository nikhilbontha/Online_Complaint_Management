
CREATE TABLE complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    category VARCHAR(50),
    description TEXT,
    status VARCHAR(20),
    created_at DATETIME
);
