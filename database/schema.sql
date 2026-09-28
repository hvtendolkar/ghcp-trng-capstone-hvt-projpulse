-- PostgreSQL Schema for ProjectPulse AI

-- Create ENUM types
CREATE TYPE project_status AS ENUM ('Opportunity', 'Active', 'On-Hold', 'Completed', 'Archived');
CREATE TYPE engagement_type AS ENUM ('Time & Material', 'Fixed-Cost', 'Retainer');
CREATE TYPE invoice_status AS ENUM ('Draft', 'Issued', 'Sent', 'Partially Paid', 'Paid', 'Overdue', 'Cancelled');

-- Users table
CREATE TABLE users (
    user_id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role VARCHAR(50) DEFAULT 'Viewer',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT user_email_index UNIQUE (email)
);

CREATE INDEX idx_user_email ON users(email);

-- Projects table
CREATE TABLE projects (
    project_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    status project_status DEFAULT 'Active',
    engagement_type engagement_type NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    contract_value DECIMAL(15, 2),
    budget DECIMAL(15, 2) NOT NULL,
    available_funding DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    client_name VARCHAR(255) NOT NULL,
    billing_manager VARCHAR(255),
    created_by VARCHAR(36) REFERENCES users(user_id),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_project_code ON projects(code);
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_project_created_by ON projects(created_by);

-- Resources table
CREATE TABLE resources (
    resource_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    designation VARCHAR(255),
    default_billable_rate DECIMAL(10, 2) NOT NULL,
    cost_rate DECIMAL(10, 2),
    availability_status VARCHAR(50) DEFAULT 'Available',
    skills JSON,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_resource_email ON resources(email);
CREATE INDEX idx_resource_designation ON resources(designation);

-- Resource Allocations table
CREATE TABLE resource_allocations (
    allocation_id VARCHAR(36) PRIMARY KEY,
    project_id VARCHAR(36) NOT NULL REFERENCES projects(project_id),
    resource_id VARCHAR(36) NOT NULL REFERENCES resources(resource_id),
    designation VARCHAR(255),
    billable_rate_override DECIMAL(10, 2),
    monthly_hours_allocation DECIMAL(10, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_allocated_hours DECIMAL(10, 2),
    ytd_billed_hours DECIMAL(10, 2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_allocation_project ON resource_allocations(project_id);
CREATE INDEX idx_allocation_resource ON resource_allocations(resource_id);

-- WBS Codes table
CREATE TABLE wbs_codes (
    wbs_id VARCHAR(36) PRIMARY KEY,
    project_id VARCHAR(36) NOT NULL REFERENCES projects(project_id),
    code VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    allocated_hours DECIMAL(10, 2),
    allocated_budget DECIMAL(15, 2),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_wbs_project ON wbs_codes(project_id);
CREATE UNIQUE INDEX idx_wbs_code_project ON wbs_codes(code, project_id);

-- Billed Hours table
CREATE TABLE billed_hours (
    billed_hours_id VARCHAR(36) PRIMARY KEY,
    allocation_id VARCHAR(36) REFERENCES resource_allocations(allocation_id),
    wbs_id VARCHAR(36) REFERENCES wbs_codes(wbs_id),
    invoice_id VARCHAR(36),
    hours_logged DECIMAL(10, 2) NOT NULL,
    date_logged DATE NOT NULL,
    description VARCHAR(255),
    cost_amount DECIMAL(15, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'Draft',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_billed_allocation ON billed_hours(allocation_id);
CREATE INDEX idx_billed_wbs ON billed_hours(wbs_id);
CREATE INDEX idx_billed_invoice ON billed_hours(invoice_id);
CREATE INDEX idx_billed_status ON billed_hours(status);

-- Milestones table
CREATE TABLE milestones (
    milestone_id VARCHAR(36) PRIMARY KEY,
    project_id VARCHAR(36) NOT NULL REFERENCES projects(project_id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    trigger_type VARCHAR(50),
    trigger_value VARCHAR(255),
    invoice_percentage DECIMAL(5, 2),
    invoice_amount DECIMAL(15, 2),
    target_date DATE,
    actual_date DATE,
    status VARCHAR(50) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_milestone_project ON milestones(project_id);
CREATE INDEX idx_milestone_status ON milestones(status);

-- Invoices table
CREATE TABLE invoices (
    invoice_id VARCHAR(36) PRIMARY KEY,
    invoice_number VARCHAR(50) UNIQUE NOT NULL,
    project_id VARCHAR(36) NOT NULL REFERENCES projects(project_id),
    milestone_id VARCHAR(36) REFERENCES milestones(milestone_id),
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    total_amount DECIMAL(15, 2) NOT NULL,
    tax_amount DECIMAL(15, 2),
    tax_rate DECIMAL(5, 2),
    discount_amount DECIMAL(15, 2),
    net_amount DECIMAL(15, 2) NOT NULL,
    status invoice_status DEFAULT 'Draft',
    payment_date DATE,
    payment_method VARCHAR(50),
    notes TEXT,
    attachment_url VARCHAR(255),
    created_by VARCHAR(36) REFERENCES users(user_id),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_invoice_number ON invoices(invoice_number);
CREATE INDEX idx_invoice_project ON invoices(project_id);
CREATE INDEX idx_invoice_status ON invoices(status);
CREATE INDEX idx_invoice_due_date ON invoices(due_date);

-- Financial Insights table (AI-generated)
CREATE TABLE financial_insights (
    insight_id VARCHAR(36) PRIMARY KEY,
    project_id VARCHAR(36) REFERENCES projects(project_id),
    insight_type VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    severity VARCHAR(50),
    recommendation TEXT,
    created_by_model VARCHAR(100) DEFAULT 'Gemma-4-26b',
    created_at TIMESTAMP DEFAULT NOW(),
    ttl INTEGER
);

CREATE INDEX idx_insight_project ON financial_insights(project_id);
CREATE INDEX idx_insight_type ON financial_insights(insight_type);
CREATE INDEX idx_insight_severity ON financial_insights(severity);

-- Audit Logs table (for Principle II compliance)
CREATE TABLE audit_logs (
    audit_id VARCHAR(36) PRIMARY KEY,
    entity_type VARCHAR(100) NOT NULL,
    entity_id VARCHAR(36) NOT NULL,
    action VARCHAR(50) NOT NULL,
    change_type VARCHAR(100),
    old_value TEXT,
    new_value TEXT,
    user_id VARCHAR(36) NOT NULL REFERENCES users(user_id),
    timestamp TIMESTAMP DEFAULT NOW(),
    justification TEXT,
    CONSTRAINT immutable_audit CHECK (true)
);

CREATE INDEX idx_audit_entity ON audit_logs(entity_type, entity_id);
CREATE INDEX idx_audit_user ON audit_logs(user_id);
CREATE INDEX idx_audit_timestamp ON audit_logs(timestamp);

-- Insert demo user (password: password123)
INSERT INTO users (user_id, email, hashed_password, full_name, role, is_active)
VALUES (
    'demo-user-id',
    'admin@company.com',
    '$2b$12$kZLV1gVYCF4o1pj7SkKlK.Oj.RZU2XUbYplJhNGGlRvLxFVqB2N8u',
    'Admin User',
    'Admin',
    true
);
