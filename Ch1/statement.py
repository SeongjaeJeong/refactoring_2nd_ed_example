import math


def statement(invoice: dict, plays: dict) -> str:
    total_amount = 0
    volume_credits = 0
    result = f'청구 내역 (고객명: {invoice["customer"]})\n'

    for perf in invoice["performances"]:
        # 포인트 적립
        volume_credits += volumeCreditsFor(plays, perf)

        # 청구 내역 출력
        result += f'\t{playFor(plays, perf)["name"]}: ${format(amountFor(perf, plays) / 100, ",")} ({perf["audience"]}석)\n'
        total_amount += amountFor(perf, plays)

    result += f'총액: ${format(total_amount / 100, ",")}\n'
    result += f"적립 포인트: {volume_credits}점"

    return result


def volumeCreditsFor(plays, aPerformance):
    result = 0
    result += max(aPerformance["audience"] - 30, 0)
    if playFor(plays, aPerformance)["type"] == "comedy":
        result += math.floor(aPerformance["audience"] / 5)
    return result


def playFor(plays, aPerformance):
    return plays[aPerformance["playID"]]


def amountFor(aPerformance, plays):
    result = 0
    if playFor(plays, aPerformance)["type"] == "tragedy":
        result = 40000
        if aPerformance["audience"] > 30:
            result += 1000 * (aPerformance["audience"] - 30)
    elif playFor(plays, aPerformance)["type"] == "comedy":
        result = 30000
        if aPerformance["audience"] > 20:
            result += 10000 + 500 * (aPerformance["audience"] - 20)
        result += 300 * aPerformance["audience"]
    else:
        raise Exception(f'알 수 없는 장르: {playFor(plays, aPerformance)["type"]}')
    return result