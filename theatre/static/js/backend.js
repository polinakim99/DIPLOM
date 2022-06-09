const all_seats=document.querySelectorAll('.row .seat')
const cta_btn=document.querySelector('button.purchase_btn')

async function contactAPI(url,body){
    const response=await fetch(url,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(body)
    })

    return response.json()
}

const perform_title=performSelect.options[performSelect.selectedIndex].id

contactAPI("/occupied/",{perform_title}).then(data=>{
    const occupied_seat=data["occupied_seats"]
    const perform_title=data["perform"]
    console.log(data)
    console.log(occupied_seat)

    const seat_LocalStorage=localStorage.getItem('selectedSeats')?JSON.parse(localStorage.getItem('selectedSeats')):null
    const perform_index=localStorage.getItem("selectedPerformIndex")

    const LS_perform=performSelect.options[perform_index].textContent

    if (LS_perform===perform_title){
        if (occupied_seat !== null && occupied_seat.length > 0){
            all_seats.forEach((seat,index)=>{
            if(occupied_seat.indexOf(index) > -1){
                    this.classList.add('occupied')
                    this.classList.remove('selected')
                }
            })
        }

        if(seat_LocalStorage !== null){
            seat_LocalStorage.forEach((seat,index)=>{
                if (occupied_seat.includes(seat)){
                    seat_LocalStorage.splice(index,1)
                    localStorage.setItem("selectedSeats",seat_LocalStorage)
                }
            })
        }
    }
    updateSelectedCount()
})
