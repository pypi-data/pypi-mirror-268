-- name: fts_search
WITH fts_scores AS (
    SELECT rowid as rowid,
           bm25(fts_terms) AS distance
      FROM fts_terms
     WHERE fts_terms MATCH :term
)
   SELECT
      'fts' as type,
      terms.slug,
      terms.label,
      terms.term,
      terms.prevalence,
      terms.is_alias,
      fts_scores.distance,
      rank() OVER (ORDER BY fts_scores.distance, terms.prevalence DESC) AS rank
   FROM fts_scores
   JOIN terms
     ON terms.rowid = fts_scores.rowid
 WHERE (:labels IS NULL OR INSTR(:labels, '|' || terms.label || '|') > 0)
  LIMIT :limit
;