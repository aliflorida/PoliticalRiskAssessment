def compare_benchmark(base_country_results, benchmark_results):
    comparison = []
    for base, bench in zip(base_country_results, benchmark_results):
        diff = base['score'] - bench['score']
        comparison.append({
            "model": base['model'],
            "base_score": base['score'],
            "benchmark_score": bench['score'],
            "difference": diff,
            "risk_higher": base['model'] if diff > 0 else "Benchmark"
        })
    return comparison