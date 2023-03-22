 function showToast(type,msg) {
    if (type=='success') {
        Swal.fire({
            title: "Success!",
            text: msg,
            icon: "success",
            showCancelButton: !0,
            confirmButtonClass: "btn btn-primary w-xs me-2 mt-2",
            cancelButtonClass: "btn btn-danger w-xs mt-2",
            buttonsStyling: !1,
            showCloseButton: !0
        })
    } else {
        Swal.fire({
            title: "Oops...",
            text: msg,
            icon: "error",
            confirmButtonClass: "btn btn-primary w-xs mt-2",
            buttonsStyling: !1,
            //footer: '<a href="">Why do I have this issue?</a>',
            showCloseButton: !0
        })
    }
     
}
