-- name: upsert-entities*!
-- Upserts entities into the entities table
INSERT OR REPLACE INTO entities
        (slug, name, label, prevalence, meta, aliases)
     VALUES
        (:slug, :name, :label, :prevalence, :meta, :aliases)
;

-- name: upsert-terms*!
-- Upserts terms into the terms table
INSERT OR REPLACE INTO terms
        (slug, label, term, is_alias, prevalence, vector)
    VALUES
        (:slug, :label, LOWER(:term), :is_alias, :prevalence, :vector)
;