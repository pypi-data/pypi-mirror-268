-- name: exact_search
SELECT
    "exact" as type,
    terms.slug,
    terms.label,
    terms.term,
    terms.is_alias,
    terms.prevalence,
    terms.is_alias as distance,
    rank() OVER (ORDER BY terms.is_alias ASC, terms.prevalence DESC) AS rank
FROM terms
WHERE terms.term = LOWER(:term)
  AND (:labels IS NULL OR INSTR(:labels, '|' || terms.label || '|') > 0)
;