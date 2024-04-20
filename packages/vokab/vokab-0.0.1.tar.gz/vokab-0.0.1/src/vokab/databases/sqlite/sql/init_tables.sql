-- name: init_tables#

-- Entities Table
CREATE TABLE IF NOT EXISTS entities (
    slug TEXT primary key,
    name TEXT NOT NULL,
    label TEXT NOT NULL,
    prevalence INTEGER,
    meta TEXT,
    aliases TEXT,
    UNIQUE (name, label)
);

-- Terms Table
CREATE TABLE IF NOT EXISTS terms (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT NOT NULL,
    label TEXT NOT NULL,
    term TEXT NOT NULL,
    is_alias INTEGER DEFAULT 0,
    prevalence INTEGER DEFAULT 0,
    vector BLOB,
    UNIQUE(slug, term),
    FOREIGN KEY (slug) REFERENCES entities(slug)
    ON DELETE CASCADE
);

-- Full Text Search
CREATE VIRTUAL TABLE IF NOT EXISTS fts_terms USING fts5(
    term,
    content='terms',
    content_rowid='rowid',
    tokenize="trigram case_sensitive 0"
);

CREATE INDEX IF NOT EXISTS idx_terms_slug ON terms (slug);
CREATE INDEX IF NOT EXISTS idx_terms_term ON terms (term);

-- Note: VSS processed in Python code due to limit of aiosql (no variables in executable scripts)
