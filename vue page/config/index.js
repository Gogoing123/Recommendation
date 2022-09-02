module.exports = {  
 proxyTable: {
    // 下面是接口的路径，我的接口 地址是http://ad.why.com/login 
    '/api': {
        // 需要转发代理的域名
        target: 'http://localhost:5000',	
        // 如果是https接口，需要配置这个参数
        secure: false,
         // 如果接口跨域，需要进行这个参数配置
        changeOrigin: true,
        // 这是一个通配符，设置完了之后每个接口都要在前面加上/api（特别注意这一点）
         pathRewrite: {
            '^/api': '/'
         }
    }
}}