import math


def statement(invoice: dict, plays: dict) -> str:
    total_amount = 0
    volume_credits = 0
    result = f'청구 내역 (고객명: {invoice["customer"]})\n'

    for perf in invoice["performances"]:
        this_amount = amountFor(perf, playFor(plays, perf))

        # 포인트 적립
        volume_credits += max(perf["audience"] - 30, 0)
        # 희극 관객 5명마다 추가 포인트 제공
        if playFor(plays, perf)["type"] == "comedy":
            volume_credits += math.floor(perf["audience"] / 5)

        # 청구 내역 출력
        result += f'\t{playFor(plays, perf)["name"]}: ${format(this_amount / 100, ",")} ({perf["audience"]}석)\n'
        total_amount += this_amount

    result += f'총액: ${format(total_amount / 100, ",")}\n'
    result += f"적립 포인트: {volume_credits}점"

    return result


def playFor(plays, aPerformance):
    return plays[aPerformance["playID"]]


def amountFor(aPerformance, play):
    result = 0
    if play["type"] == "tragedy":
        result = 40000
        if aPerformance["audience"] > 30:
            result += 1000 * (aPerformance["audience"] - 30)
    elif play["type"] == "comedy":
        result = 30000
        if aPerformance["audience"] > 20:
            result += 10000 + 500 * (aPerformance["audience"] - 20)
        result += 300 * aPerformance["audience"]
    else:
        raise Exception(f'알 수 없는 장르: {play["type"]}')
    return result