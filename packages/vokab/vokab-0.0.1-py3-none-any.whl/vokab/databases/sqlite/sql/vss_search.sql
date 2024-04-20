-- name: vss_search
with vss_scores AS (
    select rowid,
           distance
      from vss_terms
     where vss_search(vector, vss_search_params(:vector, :limit))
)
select 'vss' as type,
       slug,
       label,
       term,
       is_alias,
       prevalence,
       distance,
       rank() OVER (ORDER BY distance) as rank
  from vss_scores
  join terms
    on terms.rowid = vss_scores.rowid
 limit :limit
;

-- name: vss_search_by_label
-- Unfortunately, sqlite-vss doesn't appear to support "pre-filtering" by other columns.
-- Instead, we need to do the full vector search sort and then filter/limit in the JOIN.
with vss_scores AS (
    select rowid,
           distance
      from vss_terms
     where vss_search(vector, vss_search_params(:vector, (SELECT COUNT(*) FROM vss_terms)))
)
select 'vss' as type,
       slug,
       label,
       term,
       is_alias,
       prevalence,
       distance,
       rank() OVER (ORDER BY distance) as rank
  from vss_scores
  join terms
    on terms.rowid = vss_scores.rowid
 WHERE (:labels IS NULL OR INSTR(:labels, '|' || terms.label || '|') > 0)
 limit :limit
;
