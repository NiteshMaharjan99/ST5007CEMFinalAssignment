var shipping = '{{order.shipping}}'
    if(shipping == 'False'){
        document.getElementById('shipping-info').innerHTML =''
    }

    var form = document.getElementById('form')
    
    form.addEventListener('submit',function(e){
        e.preventDefault()
        console.log('Form submitted...')
        document.getElementById('form-button').classList.add('hidden')
        document.getElementById('payment-info').classList.remove('hidden')
    })