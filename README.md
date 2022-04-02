# docker_selenium_demo
# 运行镜像
docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.1.3-20220327
# 测试 容器中的selenium 服务
python demo.py
#