def compare_benchmark(base_outputs, benchmark_outputs):
    results = []
    for base, bench in zip(base_outputs, benchmark_outputs):
        diff = base['score'] - bench['score']
        results.append({
            "model": base['model'],
            "base_score": base['score'],
            "benchmark_score": bench['score'],
            "difference": diff,
            "risk_higher": base['model'] if diff > 0 else "Benchmark"
        })
    return results