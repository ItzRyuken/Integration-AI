CREATE DATABASE IF NOT EXISTS reai_draft_db;
USE reai_draft_db;
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('ADMIN', 'AGENT', 'TENANT') NOT NULL,
    phone VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    property_type VARCHAR(80),
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    floor_area_sqm DECIMAL(10,2) NOT NULL,
    bedrooms INT NOT NULL,
    bathrooms INT DEFAULT 0,
    monthly_rent DECIMAL(12,2),
    description TEXT,
    status ENUM('pending', 'approved', 'rejected')
        DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agent_id) REFERENCES users(user_id)
);
CREATE TABLE IF NOT EXISTS property_valuations (
    valuation_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT NOT NULL,
    estimated_monthly_rent DECIMAL(12,2),
    estimated_property_value DECIMAL(14,2),
    confidence_score DECIMAL(5,2),
    model_version VARCHAR(50),
    valuation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valuation_status VARCHAR(30) DEFAULT 'completed',
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);
CREATE TABLE IF NOT EXISTS chatbot_logs (
    chat_id INT AUTO_INCREMENT PRIMARY KEY,
    tenant_id INT NULL,
    user_message TEXT NOT NULL,
    detected_location VARCHAR(100),
    detected_bedrooms INT,
    max_budget DECIMAL(12,2),
    chatbot_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tenant_id) REFERENCES users(user_id)
);
CREATE TABLE IF NOT EXISTS ai_logs (
    ai_log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NULL,
    valuation_id INT NULL,
    request_type VARCHAR(80) NOT NULL,
    request_data JSON,
    response_data JSON,
    status VARCHAR(30) NOT NULL,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (valuation_id)
        REFERENCES property_valuations(valuation_id)
);