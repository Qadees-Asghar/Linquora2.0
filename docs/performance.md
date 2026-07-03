# Performance Notes

## Current Performance Characteristics

### Startup
- All data files are read sequentially on startup
- Time complexity: O(n) where n = total records across all files
- For typical hospital use (< 10,000 records), startup is near-instant

### Read Operations (view/search)
- In-memory dict lookup: O(1) for ID-based access
- Search by name/department: O(n) linear scan
- For small datasets (< 1000 records), performance is excellent

### Write Operations
- Every write rewrites the entire file: O(n)
- This is a known limitation of the flat-file approach
- For large datasets, this becomes slow

## Scalability Limits

| Records | Expected Performance |
|---------|---------------------|
| < 1,000 | Excellent |
| 1,000 - 10,000 | Good |
| > 10,000 | Degraded (file rewrites slow) |

## Future Optimization

Linquora v3.0.0 plans to migrate to SQLite which will provide:
- O(log n) indexed lookups
- Atomic transactions
- Much better write performance
- No full-file rewrites