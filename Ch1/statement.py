import math


def statement(invoice: dict, plays: dict) -> str:
    total_amount = 0
    result = f'청구 내역 (고객명: {invoice["customer"]})\n'

    for perf in invoice["performances"]:
        # 청구 내역 출력
        result += f'\t{playFor(perf, plays)["name"]}: ${usd(amountFor(perf, plays))} ({perf["audience"]}석)\n'
        total_amount += amountFor(perf, plays)

    result += f"총액: ${usd(total_amount)}\n"
    result += f"적립 포인트: {totalVolumeCredits(invoice, plays)}점"

    return result


def totalVolumeCredits(invoice, plays):
    volume_credits = 0
    for perf in invoice["performances"]:
        # 포인트 적립
        volume_credits += volumeCreditsFor(perf, plays)
    return volume_credits


def usd(aNumber):
    return format(aNumber / 100, ",")


def volumeCreditsFor(aPerformance, plays):
    result = 0
    result += max(aPerformance["audience"] - 30, 0)
    if playFor(aPerformance, plays)["type"] == "comedy":
        result += math.floor(aPerformance["audience"] / 5)
    return result


def playFor(aPerformance, plays):
    return plays[aPerformance["playID"]]


def amountFor(aPerformance, plays):
    result = 0
    if playFor(aPerformance, plays)["type"] == "tragedy":
        result = 40000
        if aPerformance["audience"] > 30:
            result += 1000 * (aPerformance["audience"] - 30)
    elif playFor(aPerformance, plays)["type"] == "comedy":
        result = 30000
        if aPerformance["audience"] > 20:
            result += 10000 + 500 * (aPerformance["audience"] - 20)
        result += 300 * aPerformance["audience"]
    else:
        raise Exception(f'알 수 없는 장르: {playFor(aPerformance, plays)["type"]}')
    return result