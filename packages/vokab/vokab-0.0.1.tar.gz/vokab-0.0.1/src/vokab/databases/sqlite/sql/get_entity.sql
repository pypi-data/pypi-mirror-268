-- name: get-entity^
select *
  from entities
 where slug = :slug
;