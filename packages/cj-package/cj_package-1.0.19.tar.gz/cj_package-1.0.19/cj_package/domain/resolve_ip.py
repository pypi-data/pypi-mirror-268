from loguru import logger
import dns.resolver

def get_ip_list(domain, dns_server='114.114.114.114') -> list:
    """获取域名解析出的IP列表
    @param domain: 域名
    @param dns_server: DNS服务器
    """
    max_retries = 3
    ip_set = set()
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]

    for _ in range(max_retries):
        try:
            answers = resolver.resolve(domain, 'A')  # 查询A记录
            ips = {item.address for item in answers}
            ip_set.update(ips)
        except Exception as e:
            logger.error(f'解析域名{domain}出错了，请查看: {e}')
        else:
            if ip_set:
                break

    return list(ip_set)

# print(get_ip_list('xxx.cjdropshipping.cn'))
