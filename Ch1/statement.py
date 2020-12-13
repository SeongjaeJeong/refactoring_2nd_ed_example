import math
import copy


def statement(invoice: dict, plays: dict) -> str:
    statement_data = dict()
    statement_data["customer"] = invoice["customer"]
    statement_data["performances"] = [
        enrichPerformance(perf, plays) for perf in invoice["performances"]
    ]

    return renderPlainText(statement_data, plays)


def enrichPerformance(aPerformance, plays):
    result = copy.copy(aPerformance)
    result["play"] = playFor(result, plays)
    return result


def renderPlainText(data, plays):
    result = f'청구 내역 (고객명: {data["customer"]})\n'
    for perf in data["performances"]:
        # 청구 내역 출력
        result += f'\t{perf["play"]["name"]}: ${usd(amountFor(perf, plays))} ({perf["audience"]}석)\n'
    result += f"총액: ${usd(totalAmount(data, plays))}\n"
    result += f"적립 포인트: {totalVolumeCredits(data, plays)}점"
    return result


def totalAmount(data, plays):
    result = 0
    for perf in data["performances"]:
        result += amountFor(perf, plays)
    return result


def totalVolumeCredits(data, plays):
    result = 0
    for perf in data["performances"]:
        # 포인트 적립
        result += volumeCreditsFor(perf, plays)
    return result


def usd(aNumber):
    return format(aNumber / 100, ",")


def volumeCreditsFor(aPerformance, plays):
    result = 0
    result += max(aPerformance["audience"] - 30, 0)
    if aPerformance["play"]["type"] == "comedy":
        result += math.floor(aPerformance["audience"] / 5)
    return result


def playFor(aPerformance, plays):
    return plays[aPerformance["playID"]]


def amountFor(aPerformance, plays):
    result = 0
    if aPerformance["play"]["type"] == "tragedy":
        result = 40000
        if aPerformance["audience"] > 30:
            result += 1000 * (aPerformance["audience"] - 30)
    elif aPerformance["play"]["type"] == "comedy":
        result = 30000
        if aPerformance["audience"] > 20:
            result += 10000 + 500 * (aPerformance["audience"] - 20)
        result += 300 * aPerformance["audience"]
    else:
        raise Exception(f'알 수 없는 장르: {aPerformance["play"]["type"]}')
    return result