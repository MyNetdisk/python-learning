# Python有一个名为_statistics_的模块，我们可以使用这个模块来计算统计数据。但是，让我们尝试开发一个可以计算均值、中位数、众数、标准差等统计数据的类。
from collections import Counter


class Statistics:
    def __init__(self, data=None):
        # 避免可变默认参数的陷阱：用 None 代替 []
        self.data = data if data is not None else []

    def _check_empty(self):
        """检查数据是否为空"""
        if not self.data:
            raise ValueError("数据为空，无法计算统计量。")

    def count(self):
        """求个数"""
        return len(self.data)

    def sum(self):
        """求和"""
        self._check_empty()
        return sum(self.data)

    def min(self):
        """求最小值"""
        self._check_empty()
        return min(self.data)

    def max(self):
        """求最大值"""
        self._check_empty()
        return max(self.data)

    def range(self):
        """求范围（极差）"""
        self._check_empty()
        return self.max() - self.min()

    def mean(self):
        """求均值（算术平均数）"""
        self._check_empty()
        return sum(self.data) / len(self.data)

    def median(self):
        """求中位数"""
        self._check_empty()
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    def mode(self):
        """
        求众数
        返回出现次数最多的值及其出现次数
        """
        self._check_empty()
        data_counts = Counter(self.data)
        max_count = max(data_counts.values())
        modes = [value for value, count in data_counts.items() if count == max_count]
        return {'mode': modes[0], 'count': max_count}

    def standard_deviation(self):
        """
        求总体标准差
        公式：sqrt( Σ(xi - mean)² / n )
        """
        self._check_empty()
        mean_val = self.mean()
        variance = sum((x - mean_val) ** 2 for x in self.data) / len(self.data)
        return round(variance ** 0.5, 1)

    def variance(self):
        """
        求总体方差
        公式：Σ(xi - mean)² / n
        注意：方差是标准差的平方，不需要再开方
        """
        self._check_empty()
        mean_val = self.mean()
        return round(sum((x - mean_val) ** 2 for x in self.data) / len(self.data), 1)

    def frequency_distribution(self):
        """
        求频数分布
        返回按值排序的 (值, 频数) 元组列表
        """
        self._check_empty()
        data_counts = Counter(self.data)
        return sorted(data_counts.items())

    def describe(self):
        """求描述统计，返回所有统计量的字典"""
        self._check_empty()
        return {
            "count": self.count(),
            "sum": self.sum(),
            "min": self.min(),
            "max": self.max(),
            "range": self.range(),
            "mean": round(self.mean(), 1),
            "median": self.median(),
            "mode": self.mode(),
            "standard_deviation": self.standard_deviation(),
            "variance": self.variance(),
            "frequency_distribution": self.frequency_distribution()
        }


# 测试代码
data = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
statistics = Statistics(data)
print('Count:', statistics.count())  # 25
print('Sum: ', statistics.sum())  # 730
print('Min: ', statistics.min())  # 24
print('Max: ', statistics.max())  # 38
print('Range: ', statistics.range())  # 14
print('Mean: ', statistics.mean())  # 29.2
print('Median: ', statistics.median())  # 27
print('Mode: ', statistics.mode())  # {'mode': 26, 'count': 5}
print('Standard Deviation: ', statistics.standard_deviation())  # 4.2
print('Variance: ', statistics.variance())  # 17.5
print('Frequency Distribution: ', statistics.frequency_distribution())
# [(24, 2), (25, 1), (26, 5), (27, 4), (29, 1), (31, 2), (32, 3), (33, 2), (34, 2), (37, 2), (38, 1)]
